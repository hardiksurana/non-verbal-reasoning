-- question attempt distribution
select question_type, count(question_type) from questions group by question_type;

-- number of rows for complete attempt of a quiz
select count(*) from questions q join users u on q.user_id=u.user_id group by u.user_id having count(*) >= 12;

-- duplicate users
select email, count(*) from users group by email having count(*) > 1;
SELECT a.*, b.totalCount AS Duplicate FROM users a INNER JOIN (SELECT email, COUNT(*) totalCount FROM users GROUP BY email HAVING COUNT(*) >= 2) b ON a.email = b.email;

-- list of all responses by a user
select user_id, question_id, response_id, session_id, time_taken_in_secs, machine_generated, difficulty_scale, challenging_question, feedback_timestamp from responses where user_id=64;