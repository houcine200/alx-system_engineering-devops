0x02. Shell, I/O Redirections and filters


0-hello_world
echo "Hello, World"

1-confused_smiley
echo "\"(Ôo)'"

2-hellofile
cat /etc/passwd

3-twofiles
cat /etc/passwd /etc/hosts

4-lastlines
tail -n 10 /etc/passwd

5-firstlines
head -n 10 /etc/passwd

6-third_line
head -n 3 iacta | tail -n 1

7-
echo Best School > "\\*\\\\'\"Best School\"\\'\\\\*\$\\?\\*\\*\\*\\*\\*:)"

8-
ls - la > ls_cwd_content 

9-
tail -n 1 < l1 >> l1

10- 
find . -type f -name "*.js" -delete

11-directories
find . -type d -not -name '.' | wc -l

12-newest_file
ls -t1 | head -n 10

13-unique
sort | uniq -u

14- grep root /etc/passwd
15- grep -c "bin" /etc/passwd
16- grep -A 3 "root" /etc/passwd
17- grep -v "bin" /etc/passwd
18- grep "^[A-Za-z]" /etc/ssh/sshd_config
19- tr 'Ac' 'Ze'
20- tr -d 'cC'

21-reverse
rev
22- cut -d: -f1,6 /etc/passwd | sort

100-empty_casks
find . -empty | rev | cut -d '/' -f 1 | rev

101-gifs
find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f

102-acrostic
cut -c 1 | paste -s -d ''

103-the_biggest_fan
tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev
