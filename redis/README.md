Jogo de bingo utilizando Redis para controle de cartelas de predras sorteadas.

## Script para rodar

Na pasta do projeto rode o seguinte comando:

### `python3 bingo.py`

## Script para rodar

O jogo consiste em 50 cartelas sorteadas para pessoas diferente, estas sāo guardadas no redis utilizando co comando:
### 'redis.hmset(user_hash, user_info)'

Cada cartela é composta por 15 numeros e sāo sorteadas pelo redis com o seguinte comando
### 'cartela = redis.srandmember("cartela", 15)'
### 'redis.sadd(cartela_hash, *set(cartela))'

Para a realizaçāo do sorteio das pedras no utilizamos do comando SPOP

### 'redis.spop("cartela")'

Quando o ganhador estiver com o score de 15 pontos este é o ganhador
### 'score = redis.zrange("score", 0, 0, desc=True, withscores=True)'
