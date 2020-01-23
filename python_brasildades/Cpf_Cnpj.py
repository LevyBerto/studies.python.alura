from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválido!!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválido!!!")

    def format(self):
        mascara = CPF()
        return mascara.mask(self._cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválido!!!")

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)

