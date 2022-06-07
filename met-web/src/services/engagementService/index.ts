import { setEngagements } from './engagementSlice';
import http from '../../components/common/http-common.ts';
import { AnyAction, Dispatch } from 'redux';
import UserService from '../userService';
import { Engagement } from '../../models/engagement';
import { PostEngagementRequest, PutEngagementRequest } from './types';

export const fetchAll = async (dispatch: Dispatch<AnyAction>): Promise<Engagement[]> => {
    const responseData = await http.get<Engagement[]>('/engagement/', {
        headers: {
            'Content-type': 'application/json',
            Authorization: `Bearer ${UserService.getToken()}`,
        },
    });
    dispatch(setEngagements(responseData.data));
    return responseData.data;
};

export const getEngagement = async (
    engagementId: number,
    successCallback: (data: Engagement) => void,
    errorCallback: (errorMessage: string) => void,
) => {
    try {
        if (!engagementId || isNaN(Number(engagementId))) {
            throw new Error('Invalid Engagement Id ' + engagementId);
        }

        const responseData = await http.get<Engagement>(`/engagement/${engagementId}`, {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${UserService.getToken()}`,
            },
        });
        successCallback(responseData.data);
    } catch (e: unknown) {
        let errorMessage = '';
        if (typeof e === 'string') {
            errorMessage = e.toUpperCase();
        } else if (e instanceof Error) {
            errorMessage = e.message;
        }
        errorCallback(errorMessage);
    }
};

export const postEngagement = async (
    data: PostEngagementRequest,
    successCallback: () => void,
    errorCallback: (errorMessage: string) => void,
) => {
    try {
        await http.post('/engagement/', data, {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${UserService.getToken()}`,
            },
        });
        successCallback();
    } catch (e: unknown) {
        let errorMessage = '';
        if (typeof e === 'string') {
            errorMessage = e.toUpperCase();
        } else if (e instanceof Error) {
            errorMessage = e.message;
        }
        errorCallback(errorMessage);
    }
};

export const putEngagement = async (
    data: PutEngagementRequest,
    successCallback: (data: Engagement) => void,
    errorCallback: (errorMessage: string) => void,
) => {
    try {
        const response = await http.put<Engagement>('/engagement/', data, {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${UserService.getToken()}`,
            },
        });
        successCallback(response.data);
    } catch (e: unknown) {
        let errorMessage = '';
        if (typeof e === 'string') {
            errorMessage = e.toUpperCase();
        } else if (e instanceof Error) {
            errorMessage = e.message;
        }
        errorCallback(errorMessage);
    }
};