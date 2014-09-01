Name:           ros-indigo-hector-quadrotor-controller
Version:        0.3.3
Release:        0%{?dist}
Summary:        ROS hector_quadrotor_controller package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_quadrotor_controller
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-hector-uav-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-hector-uav-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs

%description
hector_quadrotor_controller provides libraries and a node for quadrotor control
using ros_control.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.3-0
- Autogenerated by Bloom

