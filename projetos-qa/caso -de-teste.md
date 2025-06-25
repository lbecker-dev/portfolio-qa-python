# 📋 Casos de Teste - API Reqres.in

## 🔍 Teste: Listar usuários (GET /api/users?page=2)
- ✅ Esperado: status 200 OK
- ✅ Retorno: JSON com lista de usuários paginados

## 🔍 Teste: Detalhar usuário (GET /api/users/2)
- ✅ Esperado: status 200 OK
- ✅ Campos: id, email, first_name, last_name, avatar

## 🛠️ Teste: Criar usuário (POST /api/users)
- 🔸 Envio:
```json
{
  "name": "Liliane",
  "job": "QA Tester"
}
