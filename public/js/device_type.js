selectDeviceType();

function selectDeviceType() {
  $("#type").change(showDeviceQuestions);
}

function showDeviceQuestions() {
  let deviceType = $("#type").val();
  if (deviceType == "") return;
  $.ajax({
    url: "api/show_questions/" + deviceType,
    type: "get",
    async: false,
    success: function (questionList) {
      parseQuestions(questionList);
    },
  });
}

function parseQuestions(questionList) {
  let questions = questionList["questions"];
  let deviceQuestions = $("#device-questions");
  deviceQuestions.empty();
  for (let i in questions) {
    let inputType = questions[i].inputType;
    switch (inputType) {
      case "text":
        deviceQuestions.append(createTextBox(questions[i]));
      case "select":
        deviceQuestions.append(createSelectBox(questions[i]));
    }
  }
}

function createTextBox(info) {
  let label = info.label;
  let name = info.name;
  let invalid = info.invalid;
  let element =
    '<label for="' +
    name +
    '" class="col-3 col-form-label">' +
    label +
    '</label><input class="form-control" type="text" name="' +
    name +
    '" required><div class="invalid-feedback">' +
    invalid +
    "</div>";
  return element;
}

function createSelectBox(info) {}
