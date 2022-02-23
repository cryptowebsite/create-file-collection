#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: create_file

short_description: This is the module for create and fill a file.

version_added: "1.0.0"

description: This module creates a file at the specified path and inserts the passed string into it.

options:
    path:
        description: Path with name of the file
        required: true
        type: str
    content:
        description: Path with name of the file
        required: false
        type: str
author:
    - Aleksandr Khaikin <aleksandr.devops@gmail.com>
'''

EXAMPLES = r'''
- name: Test create a file and write string to it
  netology.yandex_cloud_elk.create_file:
    path: some_file.txt
    content: "Hello world"
- name: Test create empty file
  netology.yandex_cloud_elk.create_file:
    path: some_file.txt
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original path param that was passed in.
    type: str
    returned: always
    sample: 'done'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'file created'
'''

from ansible.module_utils.basic import AnsibleModule
from os import path


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='')
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    if path.exists(module.params['path']):
        result['original_message'] = 'file exist'
        result['message'] = 'file exist'
    else:
        with open(module.params['path'], 'w') as file:
            file.write(module.params['content'])
        result['original_message'] = 'file created'
        result['changed'] = True
        result['message'] = 'file created'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
