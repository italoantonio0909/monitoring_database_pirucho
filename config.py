collections_dict = {
    "baseusers": {
        "fields": [
            "_id",
            "email",
            "is_active",
            "is_staff",
            "created_at",
        ],
        "headers": [
            "Id",
            "Email",
            "Activo",
            "Personal",
            "Fecha de creación"
        ],
        "directory": "usuariosbase"
    },
    "users": {
        "fields": [
            "_id",
            "base_user",
            "name",
            "lastname",
            "identification",
            "phone",
        ],
        "headers": [
            "Id",
            "Referencia usuario base",
            "Nombres",
            "apellidos",
            "Cédula",
            "Teléfono",
        ],
        "directory": "usuarios"
    },
    "coupons": {
        "fields": [
            "_id",
            "code",
            "name",
            "organization",
            "date_expiry",
            "status"
        ],
        "headers": [
            "Id",
            "Código",
            "Nombre",
            "Referencia organization",
            "Fecha expiración",
            "Estado"
        ],
        "directory": "cupones"
    },
    "transactions": {
        "fields": [
            "_id",
            "magazine",
            "coupon",
            "branch_office",
            "date",
        ],
        "headers": [
            "Id",
            "Revista",
            "Cupón",
            "Sucursal",
            "Fecha"
        ],
        "directory": "transacciones"
    },
    "organizations": {
        "fields": [
            "_id",
            "name",
            "description"
        ],
        "headers": [
            "Id",
            "Nombre",
            "Descripción"
        ],
        "directory": "organizaciones"
    },
    "branchoffices": {
        "fields": [
            "_id",
            "base_user",
            "code",
            "name",
            "management_name",
            "organization",
            "phones",
            "address"
        ],
        "headers": [
            "Id",
            "Referencia usuario base",
            "Código",
            "Nombre",
            "Negocio",
            "Organización",
            "Teléfono",
            "Dirección"
        ],
        "directory": "sucursales"
    },

}
