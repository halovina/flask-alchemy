from marshmallow import Schema, fields, validate

class UserLoginSchema(Schema):
    username = fields.String(
        required= True,
        validate= validate.Email(error="username must be valid email addres")
    )
    password = fields.String(
        required=True,
        validate= [validate.Length(min=6, max=15)]
    )