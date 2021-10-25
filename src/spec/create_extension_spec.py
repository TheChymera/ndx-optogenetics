# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Representing optogenetics devices and surgeries""",
        name="""ndx-optogenetics""",
        version="""0.1.0""",
        author=list(map(str.strip, """Horea Christian, Ben Dichter""".split(','))),
        contact=list(map(str.strip, """ben.dichter@catalystneuro.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type('Device', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    optic_fiber_implant = NWBGroupSpec(
        neurodata_type_def='OpticFiberImplant',
        neurodata_type_inc='Device',
        doc='Optical fiber implant',
        attributes=[
            NWBAttributeSpec(
                name='angle',
                doc='angle in degrees, relative to an unangled implant axis',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='ferrule_diameter',
                doc='in mm',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='cannula_diameter',
                doc='in mm',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='length',
                doc='in mm',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='manufacturer_code',
                doc='code from manufacturer',
                dtype='text',
                required=False,
            ),
            NWBAttributeSpec(
                name='numerical_apperture',
                doc='numerical apperture',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='transmittance',
                doc='transmittance',
                dtype='float',
                required=False,
            ),
        ],
    )

    orthogonal_stereotactic_target = NWBGroupSpec(
        neurodata_type_def='OrthogonalStereotacticTarget',
        neurodata_type_inc='NWBContainer',
        doc='orthogonal stereotactic target',
        attributes=[
            NWBAttributeSpec(
                name='reference',
                doc='reference point, e.g. bregma',
                dtype='text',
                default_value='bregma',
            ),
            NWBAttributeSpec(
                name='posteroanterior',
                doc='posteroanterior coordinates in mm',
                dtype='float',
            ),
            NWBAttributeSpec(
                name='leftright',
                doc='leftright coordinates in mm',
                dtype='float',
            ),
            NWBAttributeSpec(
                name='superoinferior',
                doc='superoinferior coordinates in mm',
                dtype='float',
            ),
            NWBAttributeSpec(
                name='pitch',
                doc='pitch angle in degrees',
                dtype='float',
                default_value=0.,
            ),
            NWBAttributeSpec(
                name='yaw',
                doc='yaw angle in degrees',
                dtype='float',
                default_value=0.,
            ),
            NWBAttributeSpec(
                name='roll',
                doc='roll angle in degrees',
                dtype='float',
                default_value=0.,
            ),
            NWBAttributeSpec(
                name='depth',
                doc='depth in mm',
                dtype='float',
                required=False,
            ),
            NWBAttributeSpec(
                name='qualitative_depth_reference',
                doc='set to "dura" if the insertable is lowered to the dura before coordinate setting',
                dtype='text',
                default_value='dura',
            ),
        ]
    )

    # TODO: add all of your new data types to this list
    new_data_types = [optic_fiber_implant, orthogonal_stereotactic_target]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
