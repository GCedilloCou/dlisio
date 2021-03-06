Chapter 2 - Data Organization
=============================

Test files for testing the general layout of files, defined in Chapter 2 of
rp66v1. This includes, but not limited to segmentation between Logical- and
Visible Records, Storage Unit Labels, padbytes and garbage data.

=================================== ===========================================
File                                Description
=================================== ===========================================
1lr-in-2vrs.dlis                    A logical record spanning 2 visible records

2lr-in-vr.dlis                      2 logical records in 1 visible record

3lrs-in-vr.dlis                     A single visible record with one logical
                                    record segmented into 3 logical record
                                    segments

3lr-in-vr-one-encrypted.dlis        Single VR with with 3 logical records, one
                                    encrypted

7K-file.dlis                        Testing that files between 4 and 8 kB are
                                    read correctly.

attrs-inconsistency-type-pred.dlis  First implicit lrs expects successor, but
                                    what follows is an explicit lrs with no
                                    predecessor

incomplete-sul.dlis                 Incomplete storage unit label

incomplete-vr.dlis                  Incomplete visible record


lf-lrs-inconsistency.dlis           First implicit lrs expects successor, but
                                    what follows is a new Logical File

lf-truncated-after-lrsh.dlis        First LF is ok, second is truncated after
                                    File Header lrs

nondlis.txt                         Not a dlis file

old-vr.dlis                         Older visible record, see 2.3.6.2 Format
                                    Version of rp66v1

padbytes-bad.dlis                   Mismatch between padbyte length and logical
                                    record length. Second LR in the file is
                                    correct.

padbytes-encrypted.dlis             Explicitly formatted logical record with
                                    encrypted padbytes

padbytes-large-as-record.dlis       padbytes length == logical record length

padbytes-large-as-seg-explicit.dlis padbytes length == logical record segment
                                    length, explict record

padbytes-large-as-seg-implicit.dlis padbytes length == logical record segment
                                    length, implicit record

pre-sul-garbage.dlis                Garbage before the storage unit label

pre-sul-pre-vrl-garbage.dlis        Garbage before storage unit label and
                                    visible record

small.dlis                          Test file smaller than 4kB

too-small-record.dlis               Visible record is smaller than the minimum
                                    requirement (20Bytes)

truncated-after-lrsh.dlis           File is truncated after LRSH which expects
                                    successor

truncated-in-iflr.dlis              Truncated one byte before expected end of
                                    long IFLR

truncated-in-lrsh.dlis              File is truncated in the LRSH

truncated-in-lrsh-vr-over.dlis      File is truncated in the LRSH, VR end aligns
                                    with EOF. Extremely unlikely situation.

truncated-in-second-lr.dlis         Mismatch between visible record length and
                                    remaining bytes. Second LR truncated

truncated-lr-no-lrs-in-vr.dlis      LRS expects successor, but none comes. File
                                    is truncated. VR is also truncated

truncated-lr-no-lrs-vr-over.dlis    LRS expects successor, but none comes. File
                                    is truncated. LRS and VR ends align

truncated-on-full-lr.dlis           File is truncated on a complete LR, but not
                                    VR

wrong-lrhs.dlis                     Mismatch between logical record segment
                                    length and remaining bytes in visible
                                    record (LRSH length is bigger than VR
                                    length)

zeroed-in-1st-lr.dlis               VR is expected to contain over 1 LR. Data is
                                    zeroed from middle of 1st LR. There are 512
                                    zeroes (more than default 200 bytes
                                    findvrl value)

zeroed-in-2nd-lr.dlis               VR contains 2 LRs. Data is zeroed in the
                                    middle of 2nd LR

=================================== ===========================================
