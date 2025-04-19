from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"
app.config["WTF_CSRF_ENABLED"] = False  # Solo para pruebas con test.http


# Formulario de registro con validaciones
class RegistrationForm(FlaskForm):
    name = StringField("Nombre", 
        validators=[DataRequired(message="El nombre es obligatorio."),
                    Length(min=3, message="El nombre debe tener al menos 3 caracteres.")],
        render_kw={"placeholder": "Tu nombre"})
    
    email = StringField("Correo", 
        validators=[DataRequired(message="El correo es obligatorio."),
                    Email(message="Debes ingresar un correo válido.")],
        render_kw={"placeholder": "tucorreo@ejemplo.com"})
    
    password = PasswordField("Contraseña", 
        validators=[DataRequired(message="La contraseña es obligatoria."),
                    Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")],
        render_kw={"placeholder": "Tu contraseña"})
    
    submit = SubmitField("Registrarse")

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Aquí se mostraría un mensaje de éxito, no se guarda en DB
        flash(f"Usuario {form.name.data} registrado con éxito.", "success")
        return redirect(url_for("register"))
    return render_template("register.html.jinja2", form=form)
    
if __name__ == "__main__":
    app.run(debug=True)
