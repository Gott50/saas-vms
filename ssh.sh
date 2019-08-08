#!/bin/bash

ssh -o StrictHostKeychecking=no -tt -i saas-vm.pem ec2-user@$1
