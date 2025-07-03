# 🔒 Projeto Educacional: Análise de Ransomware em Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/AES-256-4B8BBE?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ⚠️ AVISO LEGAL
Este projeto tem **fins exclusivamente educacionais** e foi desenvolvido para:
- Estudar técnicas de criptografia
- Entender como ransomware funciona
- Desenvolver habilidades defensivas

**É estritamente proibido** o uso malicioso deste código. Consulte [DIRETRIZES ÉTICAS](/docs/ETHICAL_GUIDELINES.md).

---

## 📌 Objetivos
- Implementar criptografia AES-256 simétrica
- Criar mecanismos de descriptografia
- Documentar o processo para fins acadêmicos
- Alertar sobre riscos de ransomware

---

## 🛠️ Tecnologias
| Componente | Descrição |
|------------|-----------|
| Python 3.9+ | Linguagem principal |
| PyCryptodome | Implementação AES |
| argparse | Interface de linha de comando |

---
## 🚀 Execução Controlada
Configure ambiente isolado:

````bash
docker build -t ransomware-lab -f Dockerfile .
docker run -it --rm -v $(pwd)/tests:/app ransomware-lab
````
Teste com arquivos dummy:

````bash
python src/encrypter.py -k "chaveSegura123" -f test.txt
python src/decrypter.py -k "chaveSegura123" -f test.txt
````
