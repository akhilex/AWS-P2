pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is yes, no, or maybe", function () {
    var responseBody = pm.response.json().body;
    pm.expect(["yes", "no", "maybe"]).to.include(responseBody);
});
