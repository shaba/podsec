Name: podsec
Version: 0.1.6
Release: alt1

Summary: Set of scripts for Podman Security
License: GPLv2+
Group: Development/Other
Url: https://www.altlinux.org/Gear
BuildArch: noarch

Source: %name-%version.tar

Requires: podman >= 3.4.4
Requires: shadow-submap >= 4.5
Requires: nginx >= 1.22.1
Requires: docker-registry >= 2.8.1
Requires: pinentry-common >= 1.1.0
Requires: jq >= 1.6
Requires:yq >= 2.12.2
Requires: fuse-overlayfs >= 1.1.2.3.800011b
Requires: skopeo >= 1.9.1
Requires: sh >= 4.4.23

%description
This package contains utilities for:
- setting the most secure container application access policies
  (directory /etc/containers/)
- installation of a registry and a web server for access to image signatures
- creating a user with rights to create docker images, signing them and
  placing them in the registry
- creating users with rights to run containers in rootless mode
- downloading docker images from the oci archive, placing them
  on the local system, signing and placing them on the registry

%package k8s
Summary: Summary: Set of scripts for Kubernetes Security
Group: Development/Other
Requires: kubernetes-kubeadm >= 1.24.8
Requires: kubernetes-kubelet >= 1.24.8
Requires: kubernetes-crio >= 1.24.8
Requires: cri-tools >= 1.22.0
Requires: podsec >= 0.1.1
Requires: kubernetes-client >= 1.24.8
%filter_from_requires /\/etc\/kubernetes/d

%description k8s
This package contains utilities for:
- cluster node configurations
- generation of certificates and configuration files for users

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/podsec*
%exclude %_bindir/podsec-k8s-*
%_mandir/man?/podsec*

%files k8s
%_bindir/podsec-k8s-*
%_mandir/man?/podsec-k8s-*


%changelog
* Fri Mar 17 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.6-alt1
- 0.1.6

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.4-alt1
- 0.1.4

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.3-alt1
- 0.1.3

* Thu Mar 16 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.2-alt1
- 0.1.2

* Wed Mar 15 2023 Alexey Kostarev <kaf@altlinux.org> 0.1.1-alt1
- 0.1.1

