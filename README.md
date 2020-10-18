# Blog
> Sistem de Blog escrito com django.




![](https://imgur.com/Ess4RUnl.png)


### Funcionalidades

- Sistema de categorias
- ckeditor


## Configuração para Desenvolvimento

1. Crie o arquivo `.env` na raiz do projeto, adicione as suguintes variáveis no arquivo:

```sh
# .env
DEBUG=True
SECRET_KEY=chave_super_secreta
ALLOWED_HOSTS=127.0.0.1,.localhost
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

2. Execute a seguinte sequencia de comandos:
```sh
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```





## Histórico de lançamentos

    * Trabalho em andamento

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

[https://github.com/midnightbattles/blog](https://github.com/midnightbattles/)

## Como Contribuir

1. Faça o _fork_ do projeto (<https://github.com/midnightbattles/blog/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

