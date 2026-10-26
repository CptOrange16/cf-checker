import os
import tempfile

import netCDF4

from cfchecker.cfchecks import CFChecker


def test_list_valued_flag_meanings_does_not_crash():
    fd, path = tempfile.mkstemp(suffix='.nc')
    os.close(fd)

    try:
        with netCDF4.Dataset(path, 'w') as ds:
            ds.createDimension('x', 2)
            var = ds.createVariable('Q_FLAGS', 'i4', ('x',))
            var.setncattr('flag_meanings', ['mask_a', 'mask_b'])
            var.setncattr('flag_values', [0, 1])

        checker = CFChecker(silent=True)
        results = checker.checker(path)

        assert 'Q_FLAGS' in results['variables']
        # The checker should complete and report a validation result instead of
        # crashing with TypeError when a list is passed to the regex validator.
        assert isinstance(results['variables']['Q_FLAGS'], dict)
    finally:
        if os.path.exists(path):
            os.remove(path)
