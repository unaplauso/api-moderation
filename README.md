# Un Aplauso's moderation service

## Licencia

Este proyecto está licenciado bajo la Elastic License 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Inicialización para desarrollo

Una vez instaladas las dependencias vía `uv sync` y creado el `.env` en base al [example](.env.example):

```sh
uv run fastapi dev
```

- Por defecto, se inicia en el puerto 8000. Se puede especificar otro puerto con la flag `--port TU_PUERTO`.
- El prefix global es `/api/moderation`
