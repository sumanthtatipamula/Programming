"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.container = void 0;
const inversify_1 = require("inversify");
const types_1 = require("./types");
const UsersApiServiceImpl_1 = require("./UsersApiServiceImpl");
let container = new inversify_1.Container();
exports.container = container;
container
    .bind(types_1.Types.UserApiService)
    .to(UsersApiServiceImpl_1.UsersApiServiceImpl);
//# sourceMappingURL=inversify.config.js.map