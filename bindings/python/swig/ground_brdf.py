# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ground_brdf.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ground_brdf', [dirname(__file__)])
        except ImportError:
            import _ground_brdf
            return _ground_brdf
        if fp is not None:
            try:
                _mod = imp.load_module('_ground_brdf', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ground_brdf = swig_import_helper()
    del swig_import_helper
else:
    import _ground_brdf
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



_ground_brdf.SHARED_PTR_DISOWN_swigconstant(_ground_brdf)
SHARED_PTR_DISOWN = _ground_brdf.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.ground
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.array_with_unit
import full_physics_swig.double_with_unit
class GroundBrdfVeg(full_physics_swig.ground.Ground):
    """

    C++ includes: ground_brdf.h

    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Coeffs, Flag, Ref_points, Desc_band_names):
        """

        FullPhysics::GroundBrdfVeg::GroundBrdfVeg(const blitz::Array< double, 2 > &Coeffs, const blitz::Array< bool, 2
        > &Flag, const ArrayWithUnit< double, 1 > &Ref_points, const
        std::vector< std::string > &Desc_band_names)

        """
        _ground_brdf.GroundBrdfVeg_swiginit(self, _ground_brdf.new_GroundBrdfVeg(Coeffs, Flag, Ref_points, Desc_band_names))

    def number_spectrometer(self):
        """

        virtual const int FullPhysics::GroundBrdf::number_spectrometer() const

        """
        return _ground_brdf.GroundBrdfVeg_number_spectrometer(self)


    def weight(self, wn, spec_index):
        """

        const AutoDerivative< double > GroundBrdf::weight(const double wn, const int spec_index) const

        """
        return _ground_brdf.GroundBrdfVeg_weight(self, wn, spec_index)


    def weight_intercept(self, *args):
        """

        void GroundBrdf::weight_intercept(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_weight_intercept(self, *args)


    def weight_slope(self, *args):
        """

        void GroundBrdf::weight_slope(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_weight_slope(self, *args)


    def rahman_factor(self, *args):
        """

        void GroundBrdf::rahman_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_rahman_factor(self, *args)


    def overall_amplitude(self, *args):
        """

        void GroundBrdf::overall_amplitude(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_overall_amplitude(self, *args)


    def asymmetry_parameter(self, *args):
        """

        void GroundBrdf::asymmetry_parameter(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_asymmetry_parameter(self, *args)


    def geometric_factor(self, *args):
        """

        void GroundBrdf::geometric_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_geometric_factor(self, *args)


    def breon_factor(self, *args):
        """

        void GroundBrdf::breon_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfVeg_breon_factor(self, *args)


    def brdf_covariance(self, spec_index):
        """

        const blitz::Array< double, 2 > GroundBrdf::brdf_covariance(const int spec_index) const

        """
        return _ground_brdf.GroundBrdfVeg_brdf_covariance(self, spec_index)


    def refractive_index(self, Spec_idx):
        """

        virtual const double FullPhysics::GroundBrdf::refractive_index(const int Spec_idx) const
        Returns hard coded value of 1.5 since that is the value hardcoded into
        LIDORT. 
        """
        return _ground_brdf.GroundBrdfVeg_refractive_index(self, Spec_idx)


    def black_sky_albedo(self, Spec_index, Sza):
        """

        const double GroundBrdfVeg::black_sky_albedo(const int Spec_index, const double Sza)

        """
        return _ground_brdf.GroundBrdfVeg_black_sky_albedo(self, Spec_index, Sza)


    def albedo(self, Spec_index, Sza, Vza, Azm, Stokes_coef):
        """

        const double GroundBrdfVeg::albedo(const int Spec_index, const double Sza, const double Vza, const
        double Azm, const blitz::Array< double, 1 > &Stokes_coef)

        """
        return _ground_brdf.GroundBrdfVeg_albedo(self, Spec_index, Sza, Vza, Azm, Stokes_coef)


    def breon_type(self):
        """

        virtual const std::string FullPhysics::GroundBrdfVeg::breon_type() const
        String describing which type of Breon surface type, also makes this
        class abstract. 
        """
        return _ground_brdf.GroundBrdfVeg_breon_type(self)


    def reference_point(self, spec_index):
        """

        virtual const DoubleWithUnit FullPhysics::GroundBrdf::reference_point(const int spec_index) const
        Center wavelength that spectrally dependent parameter is referenced
        to. 
        """
        return _ground_brdf.GroundBrdfVeg_reference_point(self, spec_index)


    def state_vector_name_i(self, i):
        """

        std::string GroundBrdf::state_vector_name_i(int i) const

        """
        return _ground_brdf.GroundBrdfVeg_state_vector_name_i(self, i)


    def desc(self):
        """

        virtual std::string FullPhysics::GroundBrdf::desc() const

        """
        return _ground_brdf.GroundBrdfVeg_desc(self)

    __swig_destroy__ = _ground_brdf.delete_GroundBrdfVeg
GroundBrdfVeg.number_spectrometer = new_instancemethod(_ground_brdf.GroundBrdfVeg_number_spectrometer, None, GroundBrdfVeg)
GroundBrdfVeg.weight = new_instancemethod(_ground_brdf.GroundBrdfVeg_weight, None, GroundBrdfVeg)
GroundBrdfVeg.weight_intercept = new_instancemethod(_ground_brdf.GroundBrdfVeg_weight_intercept, None, GroundBrdfVeg)
GroundBrdfVeg.weight_slope = new_instancemethod(_ground_brdf.GroundBrdfVeg_weight_slope, None, GroundBrdfVeg)
GroundBrdfVeg.rahman_factor = new_instancemethod(_ground_brdf.GroundBrdfVeg_rahman_factor, None, GroundBrdfVeg)
GroundBrdfVeg.overall_amplitude = new_instancemethod(_ground_brdf.GroundBrdfVeg_overall_amplitude, None, GroundBrdfVeg)
GroundBrdfVeg.asymmetry_parameter = new_instancemethod(_ground_brdf.GroundBrdfVeg_asymmetry_parameter, None, GroundBrdfVeg)
GroundBrdfVeg.geometric_factor = new_instancemethod(_ground_brdf.GroundBrdfVeg_geometric_factor, None, GroundBrdfVeg)
GroundBrdfVeg.breon_factor = new_instancemethod(_ground_brdf.GroundBrdfVeg_breon_factor, None, GroundBrdfVeg)
GroundBrdfVeg.brdf_covariance = new_instancemethod(_ground_brdf.GroundBrdfVeg_brdf_covariance, None, GroundBrdfVeg)
GroundBrdfVeg.refractive_index = new_instancemethod(_ground_brdf.GroundBrdfVeg_refractive_index, None, GroundBrdfVeg)
GroundBrdfVeg.black_sky_albedo = new_instancemethod(_ground_brdf.GroundBrdfVeg_black_sky_albedo, None, GroundBrdfVeg)
GroundBrdfVeg.albedo = new_instancemethod(_ground_brdf.GroundBrdfVeg_albedo, None, GroundBrdfVeg)
GroundBrdfVeg.breon_type = new_instancemethod(_ground_brdf.GroundBrdfVeg_breon_type, None, GroundBrdfVeg)
GroundBrdfVeg.reference_point = new_instancemethod(_ground_brdf.GroundBrdfVeg_reference_point, None, GroundBrdfVeg)
GroundBrdfVeg.state_vector_name_i = new_instancemethod(_ground_brdf.GroundBrdfVeg_state_vector_name_i, None, GroundBrdfVeg)
GroundBrdfVeg.desc = new_instancemethod(_ground_brdf.GroundBrdfVeg_desc, None, GroundBrdfVeg)
GroundBrdfVeg_swigregister = _ground_brdf.GroundBrdfVeg_swigregister
GroundBrdfVeg_swigregister(GroundBrdfVeg)

class GroundBrdfSoil(full_physics_swig.ground.Ground):
    """

    C++ includes: ground_brdf.h

    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Coeffs, Flag, Ref_points, Desc_band_names):
        """

        FullPhysics::GroundBrdfSoil::GroundBrdfSoil(const blitz::Array< double, 2 > &Coeffs, const blitz::Array< bool, 2
        > &Flag, const ArrayWithUnit< double, 1 > &Ref_points, const
        std::vector< std::string > &Desc_band_names)

        """
        _ground_brdf.GroundBrdfSoil_swiginit(self, _ground_brdf.new_GroundBrdfSoil(Coeffs, Flag, Ref_points, Desc_band_names))

    def number_spectrometer(self):
        """

        virtual const int FullPhysics::GroundBrdf::number_spectrometer() const

        """
        return _ground_brdf.GroundBrdfSoil_number_spectrometer(self)


    def weight(self, wn, spec_index):
        """

        const AutoDerivative< double > GroundBrdf::weight(const double wn, const int spec_index) const

        """
        return _ground_brdf.GroundBrdfSoil_weight(self, wn, spec_index)


    def weight_intercept(self, *args):
        """

        void GroundBrdf::weight_intercept(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_weight_intercept(self, *args)


    def weight_slope(self, *args):
        """

        void GroundBrdf::weight_slope(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_weight_slope(self, *args)


    def rahman_factor(self, *args):
        """

        void GroundBrdf::rahman_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_rahman_factor(self, *args)


    def overall_amplitude(self, *args):
        """

        void GroundBrdf::overall_amplitude(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_overall_amplitude(self, *args)


    def asymmetry_parameter(self, *args):
        """

        void GroundBrdf::asymmetry_parameter(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_asymmetry_parameter(self, *args)


    def geometric_factor(self, *args):
        """

        void GroundBrdf::geometric_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_geometric_factor(self, *args)


    def breon_factor(self, *args):
        """

        void GroundBrdf::breon_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_brdf.GroundBrdfSoil_breon_factor(self, *args)


    def brdf_covariance(self, spec_index):
        """

        const blitz::Array< double, 2 > GroundBrdf::brdf_covariance(const int spec_index) const

        """
        return _ground_brdf.GroundBrdfSoil_brdf_covariance(self, spec_index)


    def refractive_index(self, Spec_idx):
        """

        virtual const double FullPhysics::GroundBrdf::refractive_index(const int Spec_idx) const
        Returns hard coded value of 1.5 since that is the value hardcoded into
        LIDORT. 
        """
        return _ground_brdf.GroundBrdfSoil_refractive_index(self, Spec_idx)


    def black_sky_albedo(self, Spec_index, Sza):
        """

        const double GroundBrdfSoil::black_sky_albedo(const int Spec_index, const double Sza)

        """
        return _ground_brdf.GroundBrdfSoil_black_sky_albedo(self, Spec_index, Sza)


    def albedo(self, Spec_index, Sza, Vza, Azm, Stokes_coef):
        """

        const double GroundBrdfSoil::albedo(const int Spec_index, const double Sza, const double Vza, const
        double Azm, const blitz::Array< double, 1 > &Stokes_coef)

        """
        return _ground_brdf.GroundBrdfSoil_albedo(self, Spec_index, Sza, Vza, Azm, Stokes_coef)


    def breon_type(self):
        """

        virtual const std::string FullPhysics::GroundBrdfSoil::breon_type() const
        String describing which type of Breon surface type, also makes this
        class abstract. 
        """
        return _ground_brdf.GroundBrdfSoil_breon_type(self)


    def reference_point(self, spec_index):
        """

        virtual const DoubleWithUnit FullPhysics::GroundBrdf::reference_point(const int spec_index) const
        Center wavelength that spectrally dependent parameter is referenced
        to. 
        """
        return _ground_brdf.GroundBrdfSoil_reference_point(self, spec_index)


    def state_vector_name_i(self, i):
        """

        std::string GroundBrdf::state_vector_name_i(int i) const

        """
        return _ground_brdf.GroundBrdfSoil_state_vector_name_i(self, i)


    def desc(self):
        """

        virtual std::string FullPhysics::GroundBrdf::desc() const

        """
        return _ground_brdf.GroundBrdfSoil_desc(self)

    __swig_destroy__ = _ground_brdf.delete_GroundBrdfSoil
GroundBrdfSoil.number_spectrometer = new_instancemethod(_ground_brdf.GroundBrdfSoil_number_spectrometer, None, GroundBrdfSoil)
GroundBrdfSoil.weight = new_instancemethod(_ground_brdf.GroundBrdfSoil_weight, None, GroundBrdfSoil)
GroundBrdfSoil.weight_intercept = new_instancemethod(_ground_brdf.GroundBrdfSoil_weight_intercept, None, GroundBrdfSoil)
GroundBrdfSoil.weight_slope = new_instancemethod(_ground_brdf.GroundBrdfSoil_weight_slope, None, GroundBrdfSoil)
GroundBrdfSoil.rahman_factor = new_instancemethod(_ground_brdf.GroundBrdfSoil_rahman_factor, None, GroundBrdfSoil)
GroundBrdfSoil.overall_amplitude = new_instancemethod(_ground_brdf.GroundBrdfSoil_overall_amplitude, None, GroundBrdfSoil)
GroundBrdfSoil.asymmetry_parameter = new_instancemethod(_ground_brdf.GroundBrdfSoil_asymmetry_parameter, None, GroundBrdfSoil)
GroundBrdfSoil.geometric_factor = new_instancemethod(_ground_brdf.GroundBrdfSoil_geometric_factor, None, GroundBrdfSoil)
GroundBrdfSoil.breon_factor = new_instancemethod(_ground_brdf.GroundBrdfSoil_breon_factor, None, GroundBrdfSoil)
GroundBrdfSoil.brdf_covariance = new_instancemethod(_ground_brdf.GroundBrdfSoil_brdf_covariance, None, GroundBrdfSoil)
GroundBrdfSoil.refractive_index = new_instancemethod(_ground_brdf.GroundBrdfSoil_refractive_index, None, GroundBrdfSoil)
GroundBrdfSoil.black_sky_albedo = new_instancemethod(_ground_brdf.GroundBrdfSoil_black_sky_albedo, None, GroundBrdfSoil)
GroundBrdfSoil.albedo = new_instancemethod(_ground_brdf.GroundBrdfSoil_albedo, None, GroundBrdfSoil)
GroundBrdfSoil.breon_type = new_instancemethod(_ground_brdf.GroundBrdfSoil_breon_type, None, GroundBrdfSoil)
GroundBrdfSoil.reference_point = new_instancemethod(_ground_brdf.GroundBrdfSoil_reference_point, None, GroundBrdfSoil)
GroundBrdfSoil.state_vector_name_i = new_instancemethod(_ground_brdf.GroundBrdfSoil_state_vector_name_i, None, GroundBrdfSoil)
GroundBrdfSoil.desc = new_instancemethod(_ground_brdf.GroundBrdfSoil_desc, None, GroundBrdfSoil)
GroundBrdfSoil_swigregister = _ground_brdf.GroundBrdfSoil_swigregister
GroundBrdfSoil_swigregister(GroundBrdfSoil)



