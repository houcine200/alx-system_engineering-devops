Shell, permissions:

0-iam_betty
su betty

1-who_am_i
id -un

2-groups
groups

3-new_owner
chown betty hello

4-empty
touch hello

5-execute
chmod u+x hello

6-multiple_permissions
chmod u+x,g+x,o+r hello

7-everybody
chmod ugo+x hello

8-James_Bond
chmod 007 hello

9-John_Doe
chmod 753 hello
