-- Naseeb Mind account storage. Run ONCE in the Supabase SQL Editor.
--
-- WHY THIS FILE IS SHORT
-- ----------------------
-- Everything a student types is one of three things: an email and password,
-- which Supabase's own auth.users holds and this schema never copies; the
-- answers to a challenge; and where they got to in a challenge they have not
-- finished. That is all. There is no name, no phone, no address, no birth date
-- and no birth year, which is the same rule the anonymous test has always
-- followed and the reason this can be handed to a fourteen year old.
--
-- ROW LEVEL SECURITY IS THE WHOLE SECURITY MODEL
-- ----------------------------------------------
-- The publishable key sits in the page source where anyone can read it. That is
-- what it is for, and it is safe ONLY because RLS is on and every policy below
-- compares auth.uid() to the row's owner. If RLS were off, that key would be a
-- public read of every student's answers. So each table enables RLS on the line
-- after it is created, and nothing here is ever granted to anon.
--
-- ATTEMPTS ARE APPEND ONLY
-- ------------------------
-- There is deliberately no update policy and no delete policy on attempts. A
-- retake next year is a NEW row, because setting who a student was beside who
-- they are is the only thing a multi year record can offer, and an update in
-- place would throw that away. Postgres denies what no policy allows, so the
-- absence below is the enforcement, not an oversight.

-- ---------------------------------------------------------------- profiles --
-- Display preferences only. Both columns change what the result page SHOWS; a
-- student who changes either is not a different person and their attempts are
-- untouched.
create table if not exists public.profiles (
  id         uuid primary key references auth.users(id) on delete cascade,
  figure     text check (figure in ('male', 'female')),
  language   text check (language in ('uz', 'ru', 'en')) default 'uz',
  created_at timestamptz not null default now()
);

alter table public.profiles enable row level security;

create policy "read own profile" on public.profiles
  for select to authenticated using (auth.uid() = id);

create policy "create own profile" on public.profiles
  for insert to authenticated with check (auth.uid() = id);

create policy "update own profile" on public.profiles
  for update to authenticated using (auth.uid() = id) with check (auth.uid() = id);

-- A row is created the moment an account is, so the app never has to handle a
-- signed in student who has no profile yet.
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
begin
  insert into public.profiles (id) values (new.id)
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ---------------------------------------------------------------- attempts --
-- One finished challenge, kept for good.
--
-- instrument_version is not decoration. The moment anyone rewords an item,
-- earlier results stop being comparable to later ones, and a comparison across
-- years is the product. Items get a new version; they are never edited in place.
--
-- answers is the source of truth. scores is a cache of what the page computed
-- from it, stored so a result screen does not have to rescore every attempt.
-- Scoring lives in one place in the browser; a second implementation in SQL
-- would be a second thing that can disagree.
create table if not exists public.attempts (
  id                 uuid primary key default gen_random_uuid(),
  user_id            uuid not null default auth.uid() references auth.users(id) on delete cascade,
  challenge          text not null,
  instrument_version text not null default '1',
  answers            jsonb not null default '{}'::jsonb,
  scores             jsonb not null default '{}'::jsonb,
  completed_at       timestamptz not null default now()
);

alter table public.attempts enable row level security;

create index if not exists attempts_owner_idx
  on public.attempts (user_id, challenge, completed_at desc);

create policy "read own attempts" on public.attempts
  for select to authenticated using (auth.uid() = user_id);

create policy "add own attempts" on public.attempts
  for insert to authenticated with check (auth.uid() = user_id);

-- No update policy and no delete policy. See the header.

-- ---------------------------------------------------------------- progress --
-- Where a student got to in a challenge they have not finished yet. One row per
-- student per challenge, overwritten as they answer, deleted when the challenge
-- completes and becomes an attempt.
--
-- This is the row that makes an account worth having: a student can start on a
-- school computer and finish on their phone. It is separate from attempts
-- precisely BECAUSE it is mutable, so the append only guarantee above is not
-- weakened to accommodate a draft.
create table if not exists public.progress (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  challenge  text not null,
  answers    jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (user_id, challenge)
);

alter table public.progress enable row level security;

create policy "read own progress" on public.progress
  for select to authenticated using (auth.uid() = user_id);

create policy "save own progress" on public.progress
  for insert to authenticated with check (auth.uid() = user_id);

create policy "update own progress" on public.progress
  for update to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "drop own progress" on public.progress
  for delete to authenticated using (auth.uid() = user_id);

-- ------------------------------------------------------------------ checks --
-- If any of these come back false, stop and fix it before the site goes live.
-- A publishable key plus RLS off is a public dump of every student's answers.
select
  relname                        as table_name,
  relrowsecurity                 as rls_enabled,
  (select count(*) from pg_policies p
    where p.schemaname = 'public' and p.tablename = c.relname) as policy_count
from pg_class c
where relnamespace = 'public'::regnamespace
  and relname in ('profiles', 'attempts', 'progress')
order by relname;
