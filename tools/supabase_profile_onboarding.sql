-- Run once in the Supabase SQL Editor before deploying profile onboarding.
-- The statements are idempotent and safe for an existing profiles table.

alter table public.profiles add column if not exists first_name text;
alter table public.profiles add column if not exists last_name text;
alter table public.profiles add column if not exists country text;
alter table public.profiles add column if not exists region text;
alter table public.profiles add column if not exists district text;
alter table public.profiles add column if not exists school text;
alter table public.profiles add column if not exists grade text;
alter table public.profiles add column if not exists profile_completed boolean not null default false;
alter table public.profiles add column if not exists profile_skipped boolean not null default false;
alter table public.profiles add column if not exists updated_at timestamptz not null default now();

update public.profiles
set profile_completed = coalesce(profile_completed, false),
    profile_skipped = coalesce(profile_skipped, false),
    updated_at = coalesce(updated_at, now())
where profile_completed is null
   or profile_skipped is null
   or updated_at is null;

alter table public.profiles enable row level security;
