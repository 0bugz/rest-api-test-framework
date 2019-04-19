from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from zb_restqa import RestTestsuiteDriver

def sample_setup(ctxt):
    print("you could do any setup that is needed for the suite")
    ctxt["test_input"] = "123"
    return ctxt

def sample_teardown(ctxt):
    ctxt.clear()
    print("you can release any resource")

def pre_test_1(ctxt):
    print("you could do any setup that is needed for the suite")
    ctxt["pre_test_1"] = "123"
    return ctxt

def post_test_1(ctxt):
    print("you could do any setup that is needed for the suite")
    ctxt["post_test_1"] = "123"
    return ctxt

driver = RestTestsuiteDriver("../tests", {
    'sample_setup': sample_setup,
    'sample_teardown': sample_teardown,
    'pre_test': pre_test_1,
    'post_test': post_test_1
})

driver.run_tests()
