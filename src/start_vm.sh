#!/bin/sh
echo $SSH_KEY > ./tmp_id
tr '_' '\n' < ./tmp_id > ./id_rsa
chmod 600 ./id_rsa
rm ./tmp_id

IP=$1
shift

echo Parameters: $@

scp -o StrictHostKeychecking=no -i ./id_rsa -r ./vm_scripts $P_USER@$IP:
ssh -o StrictHostKeychecking=no -tt -i ./id_rsa $P_USER@$IP "bash vm_scripts/start.sh $@"

