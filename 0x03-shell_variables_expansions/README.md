0x03. Shell, init files, variables and expansions
1-
echo "hello $USER"
2-
PATH=$PATH:/action
3-
echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1))
4-
printenv
5-
set
6-
BEST="School"
7-
export BEST="School"
8-
echo $((128 + $TRUEKNOWLEDGE))
9-
echo $((POWER/DIVIDE))
10-
echo $((BREATH**LOVE))
11-
echo $((2#$BINARY))
12-
echo {a..z}{a..z} | tr ' ' '\n' | grep -v "oo"
13-
printf '%.2f\n' $NUM
14-100
printf '%x\n' $DECIMAL
15-101
tr "A-Za-z" 'N-ZA-Mn-za-m'
16-102
paste -d, - - | cut -d, -f1
17-103
echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')
