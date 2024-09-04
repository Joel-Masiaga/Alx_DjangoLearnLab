## Permissions and Groups Setup

### Custom Permissions
- **Book Model Permissions:**
  - `can_view`: Permission to view books.
  - `can_create`: Permission to create books.
  - `can_edit`: Permission to edit books.
  - `can_delete`: Permission to delete books.

### Groups and Permissions
- **Editors**: `can_create`, `can_edit`
- **Viewers**: `can_view`
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

### How to Add Permissions and Groups
- Use the Django admin interface to create groups and assign permissions.
- Alternatively, run the management command `python manage.py create_groups_permissions` to set up groups and permissions programmatically.

### Testing
- Create users and assign them to different groups.
- Verify access control by logging in as users with different roles and attempting to access various parts of the application.




# Security Measures

## Configuration
- `DEBUG` is set to False for production.
- CSRF and session cookies are secured with HTTPS.
- Browser-side protections are enabled with appropriate settings.
- Content Security Policy (CSP) is configured to prevent XSS attacks.

## Forms
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## Views
- Use of Django ORM for safe database queries.
- User input is validated and sanitized using Django forms.

## Testing
- Manually tested forms for CSRF and XSS vulnerabilities.
- Consider using security tools for comprehensive testing.
