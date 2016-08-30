# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests import BaseGeneralInterfaceTest
from s3transfer.manager import TransferManager


class TestDeleteObject(BaseGeneralInterfaceTest):

    __test__ = True

    def setUp(self):
        super(TestDeleteObject, self).setUp()
        self.bucket = 'mybucket'
        self.key = 'mykey'
        self.manager = TransferManager(self.client)

    @property
    def method(self):
        """The transfer manager method to invoke i.e. upload()"""
        return self.manager.delete

    def create_call_kwargs(self):
        """The kwargs to be passed to the transfer manager method"""
        return {
            'bucket': self.bucket,
            'key': self.key,
        }

    def create_invalid_extra_args(self):
        return {
            'BadKwargs': True,
        }

    def create_stubbed_responses(self):
        """A list of stubbed responses that will cause the request to succeed

        The elements of this list is a dictionary that will be used as key
        word arguments to botocore.Stubber.add_response(). For example::

            [{'method': 'put_object', 'service_response': {}}]
        """
        return [{
            'method': 'delete_object',
            'service_response': {},
            'expected_params': {'Bucket': self.bucket, 'Key': self.key},
        }]

    def create_expected_progress_callback_info(self):
        return []
