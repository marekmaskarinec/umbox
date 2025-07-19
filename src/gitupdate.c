
#include <git2.h>
#include <stdio.h>
#include <umka_api.h>

void
git_updaterepo(UmkaStackSlot *p, UmkaStackSlot *r)
{
	char *dep = (char *)umkaGetParam(p, 0)->ptrVal;
	char *ref_str = (char *)umkaGetParam(p, 1)->ptrVal;
	char *dir = (char *)umkaGetParam(p, 2)->ptrVal;

	git_repository *repo = NULL;
	if (git_repository_open(&repo, dir) < 0) {
		r->intVal = git_clone(&repo, dep, dir, NULL);
		if (r->intVal < 0)
			return;
	}

	git_remote *remote;
	r->intVal = git_remote_lookup(&remote, repo, "origin");
	if (r->intVal < 0)
		return;
	r->intVal = git_remote_fetch(remote, NULL, NULL, NULL);
	if (r->intVal < 0)
		return;

	git_reference *ref = NULL;
	git_object *target = NULL;
	if (git_reference_dwim(&ref, repo, ref_str) == 0) {
		if (git_reference_is_branch(ref)) {
			git_reference *upstream_ref = NULL;
			r->intVal = git_branch_upstream(&upstream_ref, ref);
			if (r->intVal < 0)
				return;
			git_reference_free(ref);
			ref = upstream_ref;
		}

		r->intVal = git_reference_peel(&target, ref, GIT_OBJECT_COMMIT);
		if (r->intVal < 0)
			return;

		r->intVal = git_repository_set_head(repo, git_reference_name(ref));
		if (r->intVal < 0)
			return;
	} else {
		git_oid oid;
		r->intVal = git_oid_fromstrp(&oid, ref_str);
		if (r->intVal < 0)
			return;

		r->intVal = git_object_lookup(&target, repo, &oid, GIT_OBJECT_COMMIT);
		if (r->intVal < 0)
			return;
	}

	git_reset(repo, target, GIT_RESET_HARD, NULL);

	git_object_free(target);
	git_reference_free(ref);

	git_repository_free(repo);
}

void
git_strerror(UmkaStackSlot *p, UmkaStackSlot *r)
{
	void *umka = r->ptrVal;
	UmkaAPI *api = umkaGetAPI(umka);
	r->ptrVal = api->umkaMakeStr(umka, git_error_last()->message);
}

void
git_init(UmkaStackSlot *p, UmkaStackSlot *r)
{
	git_libgit2_init();
}
