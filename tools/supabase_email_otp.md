# Email confirmation code

The signup form expects a six-digit email code.

In Supabase Dashboard:

1. Open **Authentication → Email Templates → Confirm signup**.
2. Keep the confirmation email enabled.
3. Replace the confirmation link in the template with {{ .Token }}.
4. Save the template.

The site sends the entered email and six-digit code to Supabase Auth's email
verification endpoint. A valid code creates the session; an invalid or expired
code leaves the account closed.

For production, configure a custom SMTP provider so confirmation emails are not
limited by Supabase's trial email sender.
