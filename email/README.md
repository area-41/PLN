# Codigo em linguagem Python

### Buscador de emails em meio a um texto dado.
<br/>
Supoe-se que tenha a empresa tenha recebido uma mensagem por email, ou outra forma de texto enviado como SMS ou WhatsApp, e queira retirar o email do texto de forma automatizada.<br/>
<body><br/>
<blockquote>
import re<br/>
texto = "Oi, meu nome é João, queria saber como faço para me inscrever no curso. Meu email é joao@gmail.com.br ou então no e-mail outroemail@hotmail.com. Obrigado"<br/>
<br/>
email = "[a-z0-9]+@[a-z\.]+"<br/>
<br/>
busca = re.findall(email, texto)<br/>
<br/>
if busca:<br/>
    print(busca)<br/>
</blockquote><br/>
<code> 
  ['joao@gmail.com.br', 'outroemail@hotmail.com.']

Process finished with exit code 0</code><br/>
