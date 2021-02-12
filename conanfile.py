from conans import ConanFile, CMake, MSBuild, tools


class VCGLibConan(ConanFile):
    name = "vcg"
    requires = (("eigen/3.3.9"))
    version = "1.0.1"
    license = "GPL3"
    author = "Richard Vock vock@cs.uni-bonn.de"
    url = "https://github.com/richard-vock/vcglib"
    description = "Library for manipulation, processing, cleaning and simplifying of triangle meshes"
    topics = ("geometry")
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/vcg", src="vcg", keep_path=True)
        self.copy("*.h", dst="include/wrap", src="wrap", keep_path=True)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def export_sources(self):
        self.copy("vcg/*")
        self.copy("wrap/*")
        self.copy("CMakeLists.txt")

    def package_info(self):
        self.cpp_info.libs = ["vcg"]
