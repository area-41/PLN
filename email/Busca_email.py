import re
texto = "Oi, meu nome é João, queria saber como faço para me " \
        "inscrever no curso. Meu email é joao@gmail.com.br ou então" \
        " no e-mail outroemail@hotmail.com. Obrigado"

email = "[a-z0-9]+@[a-z\.]+"

busca = re.findall(email, texto)

if busca:
    print(busca)
