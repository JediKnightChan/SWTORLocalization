import hashlib, os
import zipfile


class AssetsSupervisor:
    def __init__(self):
        self.z = zipfile.ZipFile("Assets/Assets.zip")
        self.z = zipfile.ZipFile("Assets/Assets.zip")

    def extract_all(self):
        self.z.extractall("Assets/", pwd=b"vTmoqQldMb9LvuUhPJxi5NJQv")
        print("Extracted")

    def hash_dir(self, dir_name):
        sha_hash = hashlib.md5()
        if not os.path.exists(dir_name):
            return -1

        for root, dirs, files in os.walk(dir_name):
            for names in files:
                with open(os.path.join(root, names), "rb") as f:
                    a = hashlib.md5(f.read()).hexdigest()
                    sha_hash.update(str(a).encode("utf-8"))
        return sha_hash.hexdigest()

    def check_dir(self):
        if self.hash_dir("Assets/") != "70b9e0814eefa45a05d85ab8930cc867":
            self.extract_all()


if __name__ == '__main__':
    a = AssetsSupervisor()
    print(a.hash_dir("Assets/"))
