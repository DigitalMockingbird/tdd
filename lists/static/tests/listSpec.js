describe("list js", function() {
  beforeEach(function () {
    var form = $(
      '<form id="testform">' +
        '<input name="text" />' +
        '<div class="has-error"></div>' +
      '</form>'
    );
    $('body').append(form);

  });
  afterEach(function () {
    $('#testform').remove();
  });

  it("should hide errors on keypress", function() {
    window.Superlists.hideErrorsOnInput();
    $('#testform input').trigger('keypress');
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

  it("should not hide errors unnecessarily", function() {
    window.Superlists.hideErrorsOnInput();
    expect( $('.has-error').is(':visible') ).toBe(true);
  });

});
