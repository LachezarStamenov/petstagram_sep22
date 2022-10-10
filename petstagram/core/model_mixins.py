class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_fields, getattr(self, str_fields, None)) for str_fields in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)
