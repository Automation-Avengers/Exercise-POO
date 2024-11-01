class FormBase:
    def __init__(self, nome, email, telefone, endereco, data_nascimento, mensagem):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._endereco = endereco
        self._data_nascimento = data_nascimento
        self._mensagem = mensagem
        
    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email
    
    @property
    def telefone(self):
        return self._telefone

    @property
    def endereco(self):
        return self._endereco
        
    @property
    def data_nascimento(self):
        return self._data_nascimento
        
    @property
    def mensagem(self):
        return self._mensagem
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self._email = novo_email
  
    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento

    @mensagem.setter
    def mensagem(self, nova_mensagem):
        self._mensagem = nova_mensagem
  
    def exibir_informacoes(self):
        print("Formulário Base:")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Mensagem: {self.mensagem}\n")

class FormularioContato(FormBase):
    def __init__(self, nome, email, telefone, endereco, data_nascimento, assunto, mensagem):
        super().__init__(nome, email, telefone, endereco, data_nascimento, mensagem) 
        self._assunto = assunto
        
    @property
    def assunto(self):
        return self._assunto
    
    @assunto.setter
    def assunto(self, novo_assunto):
        self._assunto = novo_assunto
        
    def exibir_informacoes(self):
        print("Formulário Contato:")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Assunto: {self.assunto}")
        print(f"Mensagem: {self.mensagem}\n")


class FormularioLogin(FormBase):
    def __init__(self, email, senha):
        super().__init__(nome = None, email= email, telefone=None, endereco = None, data_nascimento=None, mensagem=None)
        self._senha = senha
        
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha
        
    def exibir_informacoes(self):
        print("Formulário Login:")
        print(f"Email: {self.email}")
        print(f"Senha: {self.senha}\n")
