from restqa import RestTestsuiteDriver

def sample_setup(ctxt):
    print("you could do any setup that is needed for the suite")
    ctxt["test_input"] = "123"
    return ctxt

def sample_teardown(ctxt):
    ctxt.clear()
    print("you can release any resource")

driver = RestTestsuiteDriver("../tests", {
    'sample_setup': sample_setup,
    'sample_teardown': sample_teardown
})
driver.run_tests()
