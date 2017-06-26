# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _temperature.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_temperature', [dirname(__file__)])
        except ImportError:
            import _temperature
            return _temperature
        if fp is not None:
            try:
                _mod = imp.load_module('_temperature', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _temperature = swig_import_helper()
    del swig_import_helper
else:
    import _temperature
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



_temperature.SHARED_PTR_DISOWN_swigconstant(_temperature)
SHARED_PTR_DISOWN = _temperature.SHARED_PTR_DISOWN

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

import full_physics_swig.state_vector
import full_physics_swig.generic_object
class ObservableTemperature(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _temperature.delete_ObservableTemperature
ObservableTemperature.add_observer_and_keep_reference = new_instancemethod(_temperature.ObservableTemperature_add_observer_and_keep_reference, None, ObservableTemperature)
ObservableTemperature.add_observer = new_instancemethod(_temperature.ObservableTemperature_add_observer, None, ObservableTemperature)
ObservableTemperature.remove_observer = new_instancemethod(_temperature.ObservableTemperature_remove_observer, None, ObservableTemperature)
ObservableTemperature_swigregister = _temperature.ObservableTemperature_swigregister
ObservableTemperature_swigregister(ObservableTemperature)

class ObserverTemperature(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _temperature.ObserverTemperature_swiginit(self, _temperature.new_ObserverTemperature())
    __swig_destroy__ = _temperature.delete_ObserverTemperature
ObserverTemperature.notify_update = new_instancemethod(_temperature.ObserverTemperature_notify_update, None, ObserverTemperature)
ObserverTemperature.notify_add = new_instancemethod(_temperature.ObserverTemperature_notify_add, None, ObserverTemperature)
ObserverTemperature.notify_remove = new_instancemethod(_temperature.ObserverTemperature_notify_remove, None, ObserverTemperature)
ObserverTemperature_swigregister = _temperature.ObserverTemperature_swigregister
ObserverTemperature_swigregister(ObserverTemperature)

class Temperature(full_physics_swig.state_vector.StateVectorObserver, ObservableTemperature):
    """

    This class maintains the temperature portion of the state.

    Other objects may depend on the temperature, and should be updated
    when the temperature is updated. To facilitate that, this class in an
    Oberverable, and objects can add themselves as Observers to be
    notified when the temperature is updated.

    When implementing a new class, you almost always will want to derive
    from TemperatureImpBase rather than from this class. See that class
    for a description.

    C++ includes: temperature.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _temperature.delete_Temperature

    def _v_important_pressure_level(self):
        """

        virtual ArrayWithUnit<double, 1> FullPhysics::Temperature::important_pressure_level() const
        The temperature can vary quickly over a small pressure range, e.g.

        at the tropopause and stratopause. It is important that this structure
        is included in anything using the temperature, e.g., the integration
        does to calculate the optical depth of a layer in AbsorberAbsco.

        This supplied "important" pressures where something interesting in
        the temperature may be happening.

        The default is that there are not important pressures, but a derived
        class can override this, e.g. give the ECMWF pressure levels. 
        """
        return _temperature.Temperature__v_important_pressure_level(self)


    @property
    def important_pressure_level(self):
        return self._v_important_pressure_level()


    def temperature(self, Press):
        """

        virtual AutoDerivativeWithUnit<double> FullPhysics::Temperature::temperature(const AutoDerivativeWithUnit< double > &Press) const =0
        Return the temperature at the given pressure (in Pascals)

        This is in Kelvin. 
        """
        return _temperature.Temperature_temperature(self, Press)


    def temperature_grid(self, P):
        """

        ArrayAdWithUnit< double, 1 > Temperature::temperature_grid(const Pressure &P) const
        Return temperature at the pressure grid. 
        """
        return _temperature.Temperature_temperature_grid(self, P)


    def clone(self, *args):
        """

        virtual boost::shared_ptr<Temperature> FullPhysics::Temperature::clone(const boost::shared_ptr< Pressure > &Press) const =0
        This version of clone takes a pressure to use.

        The intent is that the pressure has been cloned from the original
        pressure (although this class has no way to verify this). This allows
        sets of objects to be cloned using a common Pressure clone, e.g.
        Atmosphere. 
        """
        return _temperature.Temperature_clone(self, *args)

Temperature._v_important_pressure_level = new_instancemethod(_temperature.Temperature__v_important_pressure_level, None, Temperature)
Temperature.temperature = new_instancemethod(_temperature.Temperature_temperature, None, Temperature)
Temperature.temperature_grid = new_instancemethod(_temperature.Temperature_temperature_grid, None, Temperature)
Temperature.clone = new_instancemethod(_temperature.Temperature_clone, None, Temperature)
Temperature.__str__ = new_instancemethod(_temperature.Temperature___str__, None, Temperature)
Temperature_swigregister = _temperature.Temperature_swigregister
Temperature_swigregister(Temperature)


