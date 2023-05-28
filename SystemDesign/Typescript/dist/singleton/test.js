"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const inversify_config_1 = require("./inversify.config");
const types_1 = require("./types");
const service = inversify_config_1.container.get(types_1.Types.UserApiService);
service
    .getUsers()
    .then((user) => console.log(user))
    .catch((err) => console.log(err));
//# sourceMappingURL=test.js.map