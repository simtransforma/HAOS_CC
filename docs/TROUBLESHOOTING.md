# Troubleshooting — HAOS_CC

Problemas comuns e soluções. Os 2 primeiros são os mais frequentes.

---

## ❌ "/plugin isn't available in this environment"

**Causa:** você está na **Console web da Anthropic** (console.anthropic.com), que **não suporta plugins**. Plugins só rodam no Claude Code **CLI/desktop** local.

**Solução:**
1. Abra **PowerShell/Terminal**
2. `cd` pro seu projeto
3. Rode `claude` (o binário CLI/desktop)
4. Aí dentro `/plugin` funciona

Pra confirmar que você está no CLI certo:
```bash
claude --version
# Deve mostrar: 2.1.x (Claude Code)
```

---

## ❌ "/haos:menu" retorna "Unknown command"

**Causa A:** plugin não está instalado ou enabled.

```bash
claude plugin list
# Verifique se aparece: haos@... Status: enabled
```

Se não aparece → siga [INSTALLATION.md](INSTALLATION.md).
Se aparece mas disabled → `claude plugin enable haos`.

**Causa B:** você abriu Claude Code com `--bare`, que desabilita plugins. Saia e reabra sem essa flag.

**Causa C:** o plugin foi instalado em outro usuário Windows. Plugins têm scope `user` — confirme que está logado no mesmo usuário.

---

## ❌ Erro ao validar marketplace: "Path contains '..'"

**Causa:** `marketplace.json` tem `source: "../"` (ou qualquer path com `..`). Claude Code rejeita relative paths que sobem dirs.

**Solução:** edite `.claude-plugin/marketplace.json` e troque pra `source: "./"`. O source é resolvido relativo à pasta que contém `.claude-plugin/` (não relativo ao próprio `marketplace.json`).

---

## ❌ Erro ao instalar: "repository: Invalid input: expected string, received object"

**Causa:** `plugin.json` tem `repository` como objeto. Claude Code quer string simples.

**Solução:** em `.claude-plugin/plugin.json`, mude:
```json
"repository": {
  "type": "git",
  "url": "https://github.com/.../repo.git"
}
```
Para:
```json
"repository": "https://github.com/.../repo"
```

---

## ❌ Hooks não disparam (SessionStart/Stop/PostCompact)

**Causa A:** Python não está no PATH ou versão errada.

```bash
py -3 --version
# Deve mostrar: Python 3.10 ou superior
```

Se erro → instale Python e garanta que `py.exe` está no PATH (Windows) ou `python3` (mac/linux).

**Causa B:** o caminho `${CLAUDE_PLUGIN_ROOT}` não está sendo resolvido. Isso é raro mas pode acontecer. Verifique:

```bash
claude plugin details haos
# Em "Hooks (3)" deve mostrar: SessionStart, Stop, PostCompact
```

Se hooks não aparecem → plugin instalado mal. Reinstale.

**Causa C:** rodou Claude Code com `--bare` (skip hooks).

---

## ❌ Memory dir não é criado em `~/.claude/projects/...`

**Causa A:** permissões. Tente:

```powershell
# Windows
Test-Path "$env:USERPROFILE\.claude\projects"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\projects\test"
```

Se falhar → problema de permissão de escrita em `~/.claude`. Verifique antivirus/políticas corporativas.

**Causa B:** Python lançou exceção silenciosa no hook. Rode manualmente pra debugar:

```powershell
echo '{"session_id":"test","cwd":"C:\\seu\\projeto"}' | py -3 "$env:USERPROFILE\.claude\plugins\cache\haos\hooks\session_end.py"
```

Se der erro Python → me reporte com stack trace.

---

## ❌ Setup wizard (`/haos:setup`) não inicia ou trava

**Causa A:** Claude Code não está reconhecendo o comando — veja "Unknown command" acima.

**Causa B:** Já tem CLAUDE.md/bootstrap.md existente e o wizard está esperando confirmação. Aceite "sobrescrever" ou "cancelar" no prompt.

**Causa C:** Você invocou via `claude --print "/haos:setup"` (não-interativo). O wizard precisa de input — use sessão interativa (`claude` sozinho).

---

## ❌ Agentes não respondem como esperado / dão respostas genéricas

**Causa A:** O agente está sendo invocado mas o Claude não está usando a identidade. Verifique:

```bash
claude plugin details haos | findstr "Agents"
# Deve mostrar: Agents (29)
```

Se sim, o agent existe. Pra forçar uso:

```
/haos:cmo Por favor atue como CMO conforme definido em agents/cmo.md
```

**Causa B:** Você tem CLAUDE.md no projeto sobrepondo o comportamento. Edite ou remova.

---

## ❌ Path com acentos quebra comandos

**Causa:** algum lugar tem path com acento (`Soluções`, `é`, etc) sem aspas duplas.

**Solução:** SEMPRE use aspas duplas em paths com acentos OU mude o nome da pasta pra ASCII puro.

```powershell
# ERRADO
claude --plugin-dir C:\Pasta com Acento\plugin

# CERTO
claude --plugin-dir "C:\Pasta com Acento\plugin"
```

---

## ❌ Claude Code não acha `claude.exe` no PATH

**Causa:** instalação não adicionou ao PATH.

**Solução Windows:** binário típico em `%APPDATA%\Claude\claude-code\<versão>\claude.exe`. Adicione essa pasta ao PATH OU sempre invoque com path completo.

Pra achar:
```powershell
Get-ChildItem $env:APPDATA\Claude -Recurse -Filter claude.exe -EA SilentlyContinue | Select-Object -First 1 FullName
```

---

## ❌ Plugin instalado mas comandos não aparecem no autocomplete

**Causa:** cache do Claude Code. Saia (Ctrl+C) e reabra.

Se persistir:
```bash
claude plugin disable haos
claude plugin enable haos
```

---

## ❌ Conflito de namespace (já tenho outro plugin com `/haos:*`)

**Causa:** outro plugin usa o mesmo prefixo.

**Solução:** desabilite o outro temporariamente OU edite o `plugin.json` deste pra outro `name` (mas isso muda o namespace).

---

## 🆘 Ainda quebrado?

1. Rode o diagnóstico completo:
   ```bash
   claude --version
   claude plugin list
   claude plugin validate "C:\caminho\HAOS_CC"
   claude plugin details haos
   py -3 --version
   ```

2. Cole o output numa [issue no GitHub](https://github.com/simtransforma/HAOS_CC/issues) com label `bug`. Inclua:
   - SO (Windows 10/11, macOS, Linux + distro)
   - Versão Claude Code
   - Como instalou (marketplace community / local / --plugin-dir)
   - Mensagem de erro exata
   - O que você esperava acontecer
