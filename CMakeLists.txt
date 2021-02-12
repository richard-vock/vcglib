cmake_minimum_required(VERSION 3.8.1)
project(vcglib)

find_package(Qt5Widgets)

add_library(vcg
    "wrap/system/qgetopt.cpp"
    "wrap/ply/plylib.cpp"
)
target_compile_features(vcg PUBLIC cxx_std_11)
target_link_libraries(vcg Qt5::Widgets)
