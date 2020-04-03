Exercicio HBASE

## Exercicio 1

Resposta de cada questao seguir a sequencia de comandos

### `create 'italians', 'personal-data', 'professional-data'`
### `hbase shell italians`
### `put 'italians', '11', 'personal-data:name',  'Diego de Lima'`
### `put 'italians', '11', 'personal-data:bithday',  '1993-12-08'`
### `put 'italians', '11', 'professional-data:role',  'Developer'`
### `put 'italians', '11', 'professional-data:salary',  '4567'`
### `put 'italians', '11', 'professional-data:experience',  '4'`
### `put 'italians', '12', 'personal-data:name',  'Luigi Santorini'`
### `put 'italians', '12', 'personal-data:bithday',  '1965-09-08'`
### `put 'italians', '12', 'professional-data:role',  'Developer'`
### `put 'italians', '12', 'professional-data:salary',  '4267'`
### `put 'italians', '12', 'professional-data:experience',  '3'`
### `alter 'italians', {NAME=>'personal-data', VERSIONS=>5}`
### `put 'italians', '11', 'personal-data:name',  'Dlima'`
### `put 'italians', '11', 'personal-data:bithday',  '08/12/1993'`
### `put 'italians', '11', 'professional-data:role',  'Software Engeneer'`
### `put 'italians', '11', 'professional-data:salary',  '5000'`
### `put 'italians', '11', 'professional-data:experience',  '6'`
### `scan 'italians', {VERSIONS=>5}`
### `scan 'italians', {COLUMNS=>['personal-data:name','professional-data:role']}`
### `deleteall 'italians', '1'`
### `incr 'italians', '5', 'personal-data:age', 55`
### `incr 'italians', '5', 'personal-data:age', 1`
