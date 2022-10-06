class Formset {
  static get form_name() {
    return "needs_implementation";
  }
  static get addButton() {
    return Form.getElementById(`add_${Form.form_name()}`);
  }

  constructor(number) {
    this.number = number;
    this.parent = this.form.parentElement;
    Form.form.addEventListener("click");
    this.new_form = Form.form.cloneNode(true);
    this.parent.insertBefore(this.new_form, Form.addButton);
  }
  get form() {
    return document.getElementById(this.form_name + "_" + this.number);
  }
  get deleteButton() {}
}

class CareerFormset extends Formset {
  static form = document.getElementById("career_form_0");
  constructor(number) {
    super(number);
  }
}

class AcademicBackgroundFormset extends Formset {
  static form = document.getElementById("academic_background_form_0");
  constructor(number) {
    super(form);
  }
}
