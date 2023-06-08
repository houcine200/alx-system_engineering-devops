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

10-mirror_permissions
chmod --reference=olleh hello

11-directories_permissions
chmod -R ugo+X .

12-directory_permissions
mkdir -m 751 my_dir

13-change_group
chgrp school hello

100-change_owner_and_group
chown -hR vincent:staff .

101-symbolic_link_permissions
chown -h vincent:staff _hello

102-if_only
chown --from=guillaume betty hello
