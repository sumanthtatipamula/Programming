import 'reflect-metadata';
import { UsersApiService } from './interface';
export declare class UsersApiServiceImpl implements UsersApiService {
    getUsers(): Promise<string[]>;
}
