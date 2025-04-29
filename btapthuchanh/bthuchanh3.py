import json
import os

class Student:
    def __init__(self, name, student_id, student_class, phone, birthdate, current_address):
        self.name = name
        self.student_id = student_id
        self.student_class = student_class
        self.phone = phone
        self.birthdate = birthdate
        self.current_address = current_address

    def to_dict(self):
        return {
            "Họ tên": self.name,
            "MSSV": self.student_id,
            "Lớp": self.student_class,
            "SĐT": self.phone,
            "Ngày sinh": self.birthdate,
            "Địa chỉ hiện tại": self.current_address
        }

class Family(Student):
    def __init__(self, name, student_id, student_class, phone, birthdate, current_address,
                 family_address, father_name, mother_name):
        super().__init__(name, student_id, student_class, phone, birthdate, current_address)
        self.family_address = family_address
        self.father_name = father_name
        self.mother_name = mother_name

    def to_dict(self):
        return {
            "Thông tin sinh viên": super().to_dict(),
            "Thông tin gia đình": {
                "Địa chỉ gia đình": self.family_address,
                "Họ tên bố": self.father_name,
                "Họ tên mẹ": self.mother_name
            }
        }

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.data = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def add_student(self, student: Family):
        new_id = 1 if not self.data else self.data[-1]["id"] + 1
        self.data.append({"id": new_id, **student.to_dict()})
        self.save_data()
        print("✅ Thêm sinh viên thành công.")

    def update_student(self, id, updated_info: Family):
        for i, student in enumerate(self.data):
            if student["id"] == id:
                self.data[i] = {"id": id, **updated_info.to_dict()}
                self.save_data()
                print("✅ Cập nhật thành công.")
                return
        print("❌ Không tìm thấy sinh viên.")

    def delete_student(self, id):
        original_len = len(self.data)
        self.data = [s for s in self.data if s["id"] != id]
        if len(self.data) < original_len:
            self.save_data()
            print("✅ Xoá thành công.")
        else:
            print("❌ Không tìm thấy sinh viên để xoá.")

    def show_all(self):
        if not self.data:
            print("📭 Danh sách trống.")
            return
        for s in self.data:
            print(json.dumps(s, indent=4, ensure_ascii=False))

def input_student_data():
    name = input("Họ tên: ")
    student_id = input("MSSV: ")
    student_class = input("Lớp: ")
    phone = input("SĐT: ")
    birthdate = input("Ngày sinh (dd/mm/yyyy): ")
    current_address = input("Địa chỉ hiện tại: ")
    family_address = input("Địa chỉ gia đình: ")
    father_name = input("Họ tên bố: ")
    mother_name = input("Họ tên mẹ: ")
    return Family(name, student_id, student_class, phone, birthdate, current_address,
                  family_address, father_name, mother_name)

# ===================== MENU GIAO DIỆN =====================
def main_menu():
    manager = StudentManager()

    while True:
        print("\n====== MENU QUẢN LÝ SINH VIÊN ======")
        print("1. Thêm sinh viên")
        print("2. Sửa thông tin sinh viên")
        print("3. Xoá sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Thoát")
        choice = input("Chọn thao tác (1-5): ")

        if choice == "1":
            sv = input_student_data()
            manager.add_student(sv)

        elif choice == "2":
            id = int(input("Nhập ID sinh viên cần cập nhật: "))
            sv = input_student_data()
            manager.update_student(id, sv)

        elif choice == "3":
            id = int(input("Nhập ID sinh viên cần xoá: "))
            manager.delete_student(id)

        elif choice == "4":
            manager.show_all()

        elif choice == "5":
            print("👋 Thoát chương trình. Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
