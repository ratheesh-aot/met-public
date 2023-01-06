import { render, waitFor, screen, fireEvent } from '@testing-library/react';
import React, { ReactNode } from 'react';
import '@testing-library/jest-dom';
import { setupEnv } from '../setEnvVars';
import * as reactRedux from 'react-redux';
import * as reactRouter from 'react-router';
import * as commentService from 'services/commentService';
import * as surveyService from 'services/surveyService';
import * as submissionService from 'services/submissionService';
import { createDefaultSurvey } from 'models/survey';
import { createDefaultSubmission } from 'models/surveySubmission';
import { createDefaultComment } from 'models/comment';
import SubmissionListing from 'components/comments/admin/reviewListing';
import * as utils from 'utils';

const mockSurveyOne = {
    ...createDefaultSurvey(),
    id: 1,
    name: 'Survey One',
    engagement_id: 1,
    created_date: '2022-09-14 10:00:00',
};

const mockComment1 = {
    ...createDefaultComment(),
    id: 1,
    text: 'Mock comment text',
    survey_id: mockSurveyOne.id,
    submission_id: 1,
};
const mockSubmission1 = {
    ...createDefaultSubmission(),
    id: 1,
    survey_id: 1,
    comments: [mockComment1],
    reviewed_by: 'Mock Reviewer',
};

jest.mock('@mui/material', () => ({
    ...jest.requireActual('@mui/material'),
    Link: ({ children }: { children: ReactNode }) => {
        return <a>{children}</a>;
    },
}));

jest.mock('components/common', () => ({
    ...jest.requireActual('components/common'),
    PrimaryButton: ({ children }: { children: ReactNode }) => {
        return <button>{children}</button>;
    },
    SecondaryButton: ({ children, onClick }: { children: ReactNode; onClick: () => void }) => {
        return <button onClick={onClick}>{children}</button>;
    },
}));

describe('Comment listing tests', () => {
    jest.spyOn(reactRedux, 'useSelector').mockImplementation(() => jest.fn());
    jest.spyOn(reactRedux, 'useDispatch').mockImplementation(() => jest.fn());
    jest.spyOn(reactRouter, 'useNavigate').mockImplementation(() => jest.fn());
    jest.spyOn(reactRouter, 'useParams').mockReturnValue({ surveyId: String(mockSurveyOne.id) });
    jest.spyOn(surveyService, 'getSurvey').mockReturnValue(Promise.resolve(mockSurveyOne));
    jest.spyOn(submissionService, 'getSubmissionPage').mockReturnValue(
        Promise.resolve({
            items: [mockSubmission1],
            total: 1,
        }),
    );
    const mockGetCommentsSheet = jest
        .spyOn(commentService, 'getCommentsSheet')
        .mockReturnValue(Promise.resolve({ data: new Blob(), status: 200, statusText: '', headers: {}, config: {} }));
    const mockDownloadFile = jest.spyOn(utils, 'downloadFile').mockImplementation(() => jest.fn());

    beforeEach(() => {
        setupEnv();
    });

    test('Comment table is rendered', async () => {
        render(<SubmissionListing />);

        await waitFor(() => {
            expect(screen.getByText(`${mockSurveyOne.name} Comments`)).toBeVisible();
            expect(screen.getByText(mockSubmission1.reviewed_by)).toBeVisible();
        });
    });

    test('Export comments work', async () => {
        render(<SubmissionListing />);

        await waitFor(() => {
            expect(screen.getByText(`${mockSurveyOne.name} Comments`)).toBeVisible();
            expect(screen.getByText(mockSubmission1.reviewed_by)).toBeVisible();
        });

        const exportButton = screen.getByText('Export to CSV');
        fireEvent.click(exportButton);

        await waitFor(() => {
            expect(mockGetCommentsSheet).toHaveBeenCalledOnce();
            expect(mockDownloadFile).toHaveBeenCalledOnce();
        });
    });
});