
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

class AssemblerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Assembler")
        self.root.configure(bg="#f5f5dc")  # Beige background

        self.create_steps()

        # Load opcode table once
        self.opcode_table = self.load_opcode_table()

    def create_steps(self):
        self.step_frame = tk.Frame(self.root, bg="#f5f5dc")
        self.step_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.step_label = tk.Label(self.step_frame, text="Step 1: Enter Assembly Code", bg="#f5f5dc")
        self.step_label.pack(pady=5)

        self.input_text = scrolledtext.ScrolledText(self.step_frame, width=60, height=10, bg="#add8e6")  # Light blue
        self.input_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.run_button = tk.Button(self.step_frame, text="Run Assembler", command=self.run_assembler, bg="#add8e6")  # Light blue button
        self.run_button.pack(pady=5)

        self.pass1_frame = tk.Frame(self.step_frame, bg="#f5f5dc")
        self.pass1_frame.pack(pady=5, fill=tk.BOTH)

        self.pass1_label = tk.Label(self.pass1_frame, text="Pass 1 Output", bg="#f5f5dc")
        self.pass1_label.pack(pady=5)

        self.pass1_output = scrolledtext.ScrolledText(self.pass1_frame, width=60, height=10, bg="#add8e6", fg="black")  # Light blue
        self.pass1_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.pass2_frame = tk.Frame(self.step_frame, bg="#f5f5dc")
        self.pass2_frame.pack(pady=5, fill=tk.BOTH)

        self.pass2_label = tk.Label(self.pass2_frame, text="Pass 2 Output", bg="#f5f5dc")
        self.pass2_label.pack(pady=5)

        self.pass2_output = scrolledtext.ScrolledText(self.pass2_frame, width=60, height=10, bg="#add8e6", fg="black")  # Light blue
        self.pass2_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def load_opcode_table(self):
        opcodes = {}
        try:
            with open("optab.txt", "r") as optab_file:
                for line in optab_file:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        opcodes[parts[0]] = parts[1]
        except FileNotFoundError:
            messagebox.showerror("Error", "Opcode table file not found. Please ensure 'optab.txt' exists.")
            return {}
        return opcodes

    def run_assembler(self):
        if not self.opcode_table:
            messagebox.showerror("Error", "Cannot run assembler. Opcode table is not loaded.")
            return

        assembly_lines = self.input_text.get("1.0", tk.END).strip().splitlines()
        self.pass1_output.delete(1.0, tk.END)
        self.pass2_output.delete(1.0, tk.END)

        try:
            intermediate_output = self.pass_one(assembly_lines)
            self.pass1_output.insert(tk.END, "Pass 1 Output:\n" + intermediate_output + "\n")

            pass_two_output = self.pass_two()
            self.pass2_output.insert(tk.END, "Pass 2 Output:\n" + pass_two_output + "\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def pass_one(self, assembly_lines):
        location_counter = 0
        self.starting_address = 0
        self.symbol_table = {}
        output_lines = []

        for line in assembly_lines:
            parts = line.strip().split()
            if len(parts) == 0:
                continue

            if parts[0] == "PROGRAM" and parts[1] == "START":
                self.starting_address = int(parts[2], 16)
                location_counter = self.starting_address
                output_lines.append(f"-\t{parts[0]}\t{parts[1]}\t{parts[2]}")
                continue

            if parts[0] == "END":
                output_lines.append(f"{location_counter:X}\t-\tEND\t-")
                continue

            label = parts[0] if len(parts) > 2 and parts[0] != "-" else "-"
            opcode = parts[1] if label != "-" else parts[0]
            operand = parts[2] if label != "-" and len(parts) > 2 else parts[1] if len(parts) > 1 else "-"

            if label != "-" and label not in self.symbol_table:
                self.symbol_table[label] = f"{location_counter:X}"

            if opcode == "WORD":
                output_lines.append(f"{location_counter:X}\t{label}\t{opcode}\t{operand}")
                location_counter += 3
                continue
            elif opcode == "RESW":
                output_lines.append(f"{location_counter:X}\t{label}\t{opcode}\t-")
                location_counter += 3 * int(operand)
                continue
            elif opcode == "RESB":
                output_lines.append(f"{location_counter:X}\t{label}\t{opcode}\t-")
                location_counter += int(operand)
                continue

            if opcode not in self.opcode_table:
                raise Exception(f"Invalid opcode: {opcode}")

            output_lines.append(f"{location_counter:X}\t{label}\t{opcode}\t{operand}")
            location_counter += 3

        self.write_output_files(output_lines)
        return "\n".join(output_lines)

    def write_output_files(self, output_lines):
        with open("intermediate.txt", "w") as intermediate_file:
            intermediate_file.write("\n".join(output_lines) + "\n")

    def pass_two(self):
        intermediate_with_opcodes = self.generate_intermediate_with_opcodes()
        return intermediate_with_opcodes

    def generate_intermediate_with_opcodes(self):
        intermediate_output = []
        try:
            with open("intermediate.txt", "r") as input_file:
                for line in input_file:
                    parts = line.strip().split()
                    if len(parts) < 4:
                        continue

                    locctr = parts[0]
                    label = parts[1]
                    opcode = parts[2]
                    operand = parts[3]

                    if opcode in ["END", "RESB", "RESW", "PROGRAM", "START"]:
                        opcode_value = ""
                    elif opcode == "WORD":
                        operand_value = f"{int(operand):X}".zfill(6)
                        opcode_value = operand_value
                    else:
                        opcode_value = self.opcode_table.get(opcode, "00")
                        operand_address = self.symbol_table.get(operand, "0000")
                        opcode_value = f"{opcode_value}{operand_address.zfill(4)}"

                    intermediate_output.append(f"{locctr}\t{label}\t{opcode}\t{operand}\t{opcode_value}")

            return "\n".join(intermediate_output)
        except FileNotFoundError:
            raise Exception("Intermediate file not found.")

# Create the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = AssemblerApp(root)
    root.mainloop()