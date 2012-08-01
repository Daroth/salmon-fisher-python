from wtforms import Form, PasswordField, validators


class PasswordChangeForm(Form):
  old_password = PasswordField('Old password', [validators.Required(), validators.Length(min=8)])
  new_password_1 = PasswordField('New password', [validators.Required(), validators.Length(min=8)])
  new_password_2 = PasswordField('New password (again)', [validators.Required(), validators.Length(min=8)])
