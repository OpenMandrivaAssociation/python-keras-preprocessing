%global module keras-preprocessing
%global mod %(m=%{module}; echo ${m:0:1})

Summary:	Data preprocessing and data augmentation module for Keras
Name:		python-%{module}
Version:	1.1.2
Release:	1
Source0:	https://github.com/keras-team/keras-preprocessing/archive/refs/tags/%{version}/%{module}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/%{mod}/%{module}/%{module}-%{version}.tar.gz
License:	Expat
Group:		Development/Python
Url:		https://keras.io/
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(python-distutils-extra)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(setuptools)

BuildArch:	noarch

%description
Keras is a deep learning API written in Python, running on top of the
machine learning platform TensorFlow. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result as
fast as possible is key to doing good research.

Keras is:
  - Simple   -- but not simplistic. Keras reduces developer cognitive
                load to free you to focus on the parts of the problem
                that really matter.
  - Flexible -- Keras adopts the principle of progressive disclosure
                of complexity: simple workflows should be quick and
                easy, while arbitrarily advanced workflows should be
                possible via a clear path that builds upon what you've
                already learned.
  - Powerful -- Keras provides industry-strength performance and
                scalability: it is used by organizations and companies
                including NASA, YouTube, or Waymo.

Keras Preprocessing is the data preprocessing and data augmentation
module of the Keras deep learning library. It provides utilities for
working with image data, text data, and sequence data.

%files
%license LICENSE
%doc README.md CONTRIBUTING.md PULL_REQUEST_TEMPLATE.md
%{py3_puresitedir}/keras_preprocessing
%{py3_puresitedir}/*.egg-info/

#-----------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install
