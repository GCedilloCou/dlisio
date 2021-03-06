import logging

from .. import core

class logical_file():
    """ Logical File (LF)

    This class is the main interface for working with a single LF. A LF is
    essentially a series of Logical Records (LR). There are many different LR
    types, each designed to carry a specific piece of information. For example
    a Logical File Header Record contains static information about the file,
    while the Data Format Specification Records contain information about
    curve-data, and how that should be parsed.

    This class provides an interface for easy interaction and extraction of the
    various Logical Records within the Logical File. It is completely
    independent of other LF's, and even has its own IO-device. It stores a
    pre-built index of all LR's for random access when reading from disk.

    Notes
    -----

    No parsed records are cached by this class. Thus it's advisable that the
    result of each record read is cached locally.
    """
    def __init__(self, path, io, index):
        self.path  = path
        self.io    = io
        self.index = index

    def close(self):
        self.io.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __repr__(self):
        msg = 'logical_file(path="{}", io={}, index={})'
        return msg.format(self.path, self.io, self.index)

    @property
    def header(self):
        """ Logical File Header

        """
        pass

    @property
    def trailer(self):
        """ Logical File Trailer

        Returns the Logical File Trailer - if present. Otherwise returns None.

        Returns
        -------

        trailer : dlisio.core.log_file_trailer or None


        """
        pass

    def parse_record(self, recinfo):
        # This can be C++ function (although what about the return type?)
        rec = self.io.read_record(recinfo)

        rtype = recinfo.type
        types = core.lis_rectype
        if rtype == types.data_format_spec: return core.parse_dfsr(rec)
        else:
            raise NotImplementedError("No parsing rule for  {}".format(rtype))

    def explicits(self):
        return self.index.explicits()

    def dfsr(self):
        # TODO duplication checking
        ex = self.explicits()
        recs = [x for x in ex if x.type == core.lis_rectype.data_format_spec]
        return [self.parse_record(x) for x in recs]

class physical_file(tuple):
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        for f in self:
            f.close()

    def __repr__(self):
        return 'physical_file(logical files: {})'.format(len(self))

